# EMA Hourly Continuation — WAVES/USDT P34_144

**Symbol:** WAVES/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 618 |
| net_profit_factor | 0.5161 |
| net_win_rate | 0.4385 |
| gross_profit_factor | 0.8931 |
| gross_win_rate | 0.4547 |
| sharpe_ratio | -5.7241 |
| sortino_ratio | -2.0006 |
| max_drawdown | 0.9196 |
| cagr | -0.6272 |
| net_avg_win | 36.0469 |
| net_avg_loss | -54.5521 |
| avg_hold_time_bars | 13.7346 |
| exposure | 0.3858 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
