# EMA Hourly Continuation — SEI/USDT P89_144

**Symbol:** SEI/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 0.8413 |
| net_win_rate | 0.5250 |
| gross_profit_factor | 1.0925 |
| gross_win_rate | 0.5250 |
| sharpe_ratio | -0.8087 |
| sortino_ratio | -0.1807 |
| max_drawdown | 0.3248 |
| cagr | -0.0806 |
| net_avg_win | 80.0175 |
| net_avg_loss | -105.1232 |
| avg_hold_time_bars | 7.8750 |
| exposure | 0.0859 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
