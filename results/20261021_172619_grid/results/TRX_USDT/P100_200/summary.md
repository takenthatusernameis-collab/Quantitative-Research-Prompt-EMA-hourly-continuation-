# EMA Hourly Continuation — TRX/USDT P100_200

**Symbol:** TRX/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 214 |
| net_profit_factor | 0.3994 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 0.8421 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -3.8426 |
| sortino_ratio | -0.8148 |
| max_drawdown | 0.6193 |
| cagr | -0.3169 |
| net_avg_win | 41.3737 |
| net_avg_loss | -89.1784 |
| avg_hold_time_bars | 13.4766 |
| exposure | 0.1311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
