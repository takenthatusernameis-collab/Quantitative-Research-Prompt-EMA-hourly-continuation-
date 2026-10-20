# EMA Hourly Continuation — AXL/USDT P50_200

**Symbol:** AXL/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.6982 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.9289 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -2.4443 |
| sortino_ratio | -0.7202 |
| max_drawdown | 0.5885 |
| cagr | -0.2872 |
| net_avg_win | 63.5612 |
| net_avg_loss | -83.4548 |
| avg_hold_time_bars | 19.5195 |
| exposure | 0.3860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
