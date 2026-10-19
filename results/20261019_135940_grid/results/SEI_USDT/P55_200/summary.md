# EMA Hourly Continuation — SEI/USDT P55_200

**Symbol:** SEI/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.8078 |
| net_win_rate | 0.5223 |
| gross_profit_factor | 1.0812 |
| gross_win_rate | 0.5223 |
| sharpe_ratio | -1.2054 |
| sortino_ratio | -0.3137 |
| max_drawdown | 0.3575 |
| cagr | -0.1386 |
| net_avg_win | 74.6189 |
| net_avg_loss | -100.9836 |
| avg_hold_time_bars | 24.2641 |
| exposure | 0.3717 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
