# EMA Hourly Continuation — SKL/USDT P12_34

**Symbol:** SKL/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1382 |
| net_profit_factor | 0.5235 |
| net_win_rate | 0.4559 |
| gross_profit_factor | 0.9625 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -8.7259 |
| sortino_ratio | -4.5533 |
| max_drawdown | 0.9967 |
| cagr | -0.8961 |
| net_avg_win | 17.3790 |
| net_avg_loss | -27.8123 |
| avg_hold_time_bars | 4.0326 |
| exposure | 0.2533 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
