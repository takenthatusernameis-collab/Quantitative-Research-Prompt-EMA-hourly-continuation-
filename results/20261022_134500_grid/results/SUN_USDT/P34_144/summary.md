# EMA Hourly Continuation — SUN/USDT P34_144

**Symbol:** SUN/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.3994 |
| net_win_rate | 0.3941 |
| gross_profit_factor | 0.8308 |
| gross_win_rate | 0.4282 |
| sharpe_ratio | -6.5493 |
| sortino_ratio | -1.9144 |
| max_drawdown | 0.9241 |
| cagr | -0.6364 |
| net_avg_win | 35.4435 |
| net_avg_loss | -57.7155 |
| avg_hold_time_bars | 20.9157 |
| exposure | 0.4155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
