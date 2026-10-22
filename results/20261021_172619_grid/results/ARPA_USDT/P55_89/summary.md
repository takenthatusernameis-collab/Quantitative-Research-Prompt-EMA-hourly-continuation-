# EMA Hourly Continuation — ARPA/USDT P55_89

**Symbol:** ARPA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.5356 |
| net_win_rate | 0.4430 |
| gross_profit_factor | 0.7851 |
| gross_win_rate | 0.4456 |
| sharpe_ratio | -3.8168 |
| sortino_ratio | -1.0822 |
| max_drawdown | 0.7244 |
| cagr | -0.3910 |
| net_avg_win | 47.0417 |
| net_avg_loss | -69.8652 |
| avg_hold_time_bars | 6.8304 |
| exposure | 0.1221 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
