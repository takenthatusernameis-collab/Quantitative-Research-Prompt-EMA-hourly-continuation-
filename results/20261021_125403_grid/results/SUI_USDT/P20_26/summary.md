# EMA Hourly Continuation — SUI/USDT P20_26

**Symbol:** SUI/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 164 |
| net_profit_factor | 0.7413 |
| net_win_rate | 0.5061 |
| gross_profit_factor | 1.0209 |
| gross_win_rate | 0.5061 |
| sharpe_ratio | -1.1872 |
| sortino_ratio | -0.2187 |
| max_drawdown | 0.2528 |
| cagr | -0.0948 |
| net_avg_win | 76.3879 |
| net_avg_loss | -105.5831 |
| avg_hold_time_bars | 4.7256 |
| exposure | 0.0352 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
