# EMA Hourly Continuation — WIN/USDT P21_26

**Symbol:** WIN/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 145 |
| net_profit_factor | 0.6639 |
| net_win_rate | 0.5172 |
| gross_profit_factor | 1.0956 |
| gross_win_rate | 0.5172 |
| sharpe_ratio | -1.5769 |
| sortino_ratio | -0.2750 |
| max_drawdown | 0.3038 |
| cagr | -0.1175 |
| net_avg_win | 70.9902 |
| net_avg_loss | -114.5612 |
| avg_hold_time_bars | 5.2897 |
| exposure | 0.0349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
