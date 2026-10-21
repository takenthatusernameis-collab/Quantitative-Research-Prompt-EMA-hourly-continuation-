# EMA Hourly Continuation — KSM/USDT P20_26

**Symbol:** KSM/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 0.5475 |
| net_win_rate | 0.4565 |
| gross_profit_factor | 0.8268 |
| gross_win_rate | 0.4565 |
| sharpe_ratio | -2.7414 |
| sortino_ratio | -0.5960 |
| max_drawdown | 0.4991 |
| cagr | -0.2379 |
| net_avg_win | 56.9797 |
| net_avg_loss | -87.4281 |
| avg_hold_time_bars | 4.1565 |
| exposure | 0.0435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
