# EMA Hourly Continuation — ZEN/USDT P8_144

**Symbol:** ZEN/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.7775 |
| net_win_rate | 0.5234 |
| gross_profit_factor | 1.1085 |
| gross_win_rate | 0.5280 |
| sharpe_ratio | -1.5261 |
| sortino_ratio | -0.4448 |
| max_drawdown | 0.4509 |
| cagr | -0.1944 |
| net_avg_win | 65.3448 |
| net_avg_loss | -92.2845 |
| avg_hold_time_bars | 40.3505 |
| exposure | 0.7850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
