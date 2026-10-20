# EMA Hourly Continuation — DGB/USDT P21_200

**Symbol:** DGB/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.7051 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.9678 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -2.8897 |
| sortino_ratio | -0.9136 |
| max_drawdown | 0.7031 |
| cagr | -0.3506 |
| net_avg_win | 66.4946 |
| net_avg_loss | -85.3387 |
| avg_hold_time_bars | 26.1876 |
| exposure | 0.5964 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
