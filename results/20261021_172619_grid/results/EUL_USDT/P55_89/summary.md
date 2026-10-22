# EMA Hourly Continuation — EUL/USDT P55_89

**Symbol:** EUL/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.5250 |
| net_win_rate | 0.4301 |
| gross_profit_factor | 0.7209 |
| gross_win_rate | 0.4301 |
| sharpe_ratio | -3.0848 |
| sortino_ratio | -0.7414 |
| max_drawdown | 0.5860 |
| cagr | -0.2885 |
| net_avg_win | 51.6327 |
| net_avg_loss | -74.2138 |
| avg_hold_time_bars | 8.0035 |
| exposure | 0.1040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
