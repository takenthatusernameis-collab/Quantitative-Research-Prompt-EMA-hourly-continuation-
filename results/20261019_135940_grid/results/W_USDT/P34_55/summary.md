# EMA Hourly Continuation — W/USDT P34_55

**Symbol:** W/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 868 |
| net_profit_factor | 0.4990 |
| net_win_rate | 0.4597 |
| gross_profit_factor | 0.8921 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -6.6049 |
| sortino_ratio | -2.7338 |
| max_drawdown | 0.9681 |
| cagr | -0.7426 |
| net_avg_win | 24.1407 |
| net_avg_loss | -41.1535 |
| avg_hold_time_bars | 3.1164 |
| exposure | 0.1230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
