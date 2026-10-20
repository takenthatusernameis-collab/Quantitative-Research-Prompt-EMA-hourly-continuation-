# EMA Hourly Continuation — GMX/USDT P89_144

**Symbol:** GMX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.4938 |
| net_win_rate | 0.4361 |
| gross_profit_factor | 0.8278 |
| gross_win_rate | 0.4474 |
| sharpe_ratio | -5.1735 |
| sortino_ratio | -1.6932 |
| max_drawdown | 0.8687 |
| cagr | -0.5543 |
| net_avg_win | 36.5179 |
| net_avg_loss | -57.1935 |
| avg_hold_time_bars | 5.2105 |
| exposure | 0.1260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
