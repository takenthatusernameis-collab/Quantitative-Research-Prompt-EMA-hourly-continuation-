# EMA Hourly Continuation — FLR/USDT P20_21

**Symbol:** FLR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 163 |
| net_profit_factor | 0.3955 |
| net_win_rate | 0.3742 |
| gross_profit_factor | 0.6025 |
| gross_win_rate | 0.3742 |
| sharpe_ratio | -3.6416 |
| sortino_ratio | -0.6664 |
| max_drawdown | 0.5648 |
| cagr | -0.2663 |
| net_avg_win | 57.9727 |
| net_avg_loss | -87.6601 |
| avg_hold_time_bars | 4.4969 |
| exposure | 0.0333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
