# EMA Hourly Continuation — GRT/USDT P8_34

**Symbol:** GRT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1359 |
| net_profit_factor | 0.5266 |
| net_win_rate | 0.4518 |
| gross_profit_factor | 0.9139 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -8.5352 |
| sortino_ratio | -4.3932 |
| max_drawdown | 0.9961 |
| cagr | -0.8865 |
| net_avg_win | 18.0421 |
| net_avg_loss | -28.2370 |
| avg_hold_time_bars | 5.3775 |
| exposure | 0.3307 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
