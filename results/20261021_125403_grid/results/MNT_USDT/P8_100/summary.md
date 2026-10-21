# EMA Hourly Continuation — MNT/USDT P8_100

**Symbol:** MNT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.8258 |
| net_win_rate | 0.5156 |
| gross_profit_factor | 1.0480 |
| gross_win_rate | 0.5156 |
| sharpe_ratio | -1.1514 |
| sortino_ratio | -0.3499 |
| max_drawdown | 0.3587 |
| cagr | -0.1512 |
| net_avg_win | 69.2893 |
| net_avg_loss | -89.3151 |
| avg_hold_time_bars | 33.8326 |
| exposure | 0.6890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
