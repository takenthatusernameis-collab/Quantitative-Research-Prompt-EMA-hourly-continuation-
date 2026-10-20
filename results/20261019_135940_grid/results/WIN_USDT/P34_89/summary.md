# EMA Hourly Continuation — WIN/USDT P34_89

**Symbol:** WIN/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.4155 |
| net_win_rate | 0.4356 |
| gross_profit_factor | 0.8573 |
| gross_win_rate | 0.4600 |
| sharpe_ratio | -6.6379 |
| sortino_ratio | -2.3207 |
| max_drawdown | 0.9482 |
| cagr | -0.6894 |
| net_avg_win | 25.2128 |
| net_avg_loss | -46.8243 |
| avg_hold_time_bars | 8.9984 |
| exposure | 0.2507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
