# EMA Hourly Continuation — UQC/USDT P12_55

**Symbol:** UQC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.4231 |
| net_win_rate | 0.3346 |
| gross_profit_factor | 0.5760 |
| gross_win_rate | 0.3420 |
| sharpe_ratio | -4.6825 |
| sortino_ratio | -1.0748 |
| max_drawdown | 0.7203 |
| cagr | -0.3945 |
| net_avg_win | 58.5071 |
| net_avg_loss | -69.5210 |
| avg_hold_time_bars | 51.9517 |
| exposure | 0.6325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
