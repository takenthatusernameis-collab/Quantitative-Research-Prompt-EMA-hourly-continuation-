# EMA Hourly Continuation — NEO/USDT P26_144

**Symbol:** NEO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.6131 |
| net_win_rate | 0.4761 |
| gross_profit_factor | 0.9278 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -3.1259 |
| sortino_ratio | -0.9488 |
| max_drawdown | 0.7100 |
| cagr | -0.3599 |
| net_avg_win | 48.7549 |
| net_avg_loss | -72.2625 |
| avg_hold_time_bars | 24.6870 |
| exposure | 0.5162 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
