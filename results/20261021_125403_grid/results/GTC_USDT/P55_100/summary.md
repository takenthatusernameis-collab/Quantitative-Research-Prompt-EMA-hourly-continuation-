# EMA Hourly Continuation — GTC/USDT P55_100

**Symbol:** GTC/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.6787 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.9133 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -2.5217 |
| sortino_ratio | -0.7205 |
| max_drawdown | 0.5928 |
| cagr | -0.2826 |
| net_avg_win | 62.5759 |
| net_avg_loss | -83.4574 |
| avg_hold_time_bars | 8.6269 |
| exposure | 0.1576 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
