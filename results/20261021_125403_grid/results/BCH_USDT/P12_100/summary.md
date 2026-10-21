# EMA Hourly Continuation — BCH/USDT P12_100

**Symbol:** BCH/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.7475 |
| net_win_rate | 0.4816 |
| gross_profit_factor | 0.9729 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -2.3228 |
| sortino_ratio | -0.7121 |
| max_drawdown | 0.6120 |
| cagr | -0.2788 |
| net_avg_win | 74.6483 |
| net_avg_loss | -92.7652 |
| avg_hold_time_bars | 24.4707 |
| exposure | 0.5128 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
