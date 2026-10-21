# EMA Hourly Continuation — DEEP/USDT P8_89

**Symbol:** DEEP/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.9689 |
| net_win_rate | 0.5302 |
| gross_profit_factor | 1.1153 |
| gross_win_rate | 0.5302 |
| sharpe_ratio | -0.1530 |
| sortino_ratio | -0.0469 |
| max_drawdown | 0.2153 |
| cagr | -0.0292 |
| net_avg_win | 93.3845 |
| net_avg_loss | -108.7872 |
| avg_hold_time_bars | 31.3159 |
| exposure | 0.6454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
