# EMA Hourly Continuation — YGG/USDT P26_89

**Symbol:** YGG/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.8408 |
| net_win_rate | 0.5106 |
| gross_profit_factor | 1.0564 |
| gross_win_rate | 0.5106 |
| sharpe_ratio | -1.3741 |
| sortino_ratio | -0.4493 |
| max_drawdown | 0.4659 |
| cagr | -0.1883 |
| net_avg_win | 81.2387 |
| net_avg_loss | -100.7867 |
| avg_hold_time_bars | 12.4242 |
| exposure | 0.2929 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
