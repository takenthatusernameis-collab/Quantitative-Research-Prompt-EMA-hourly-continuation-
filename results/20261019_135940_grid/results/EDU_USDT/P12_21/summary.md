# EMA Hourly Continuation — EDU/USDT P12_21

**Symbol:** EDU/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1481 |
| net_profit_factor | 0.3281 |
| net_win_rate | 0.4072 |
| gross_profit_factor | 0.7234 |
| gross_win_rate | 0.4267 |
| sharpe_ratio | -11.5858 |
| sortino_ratio | -6.3387 |
| max_drawdown | 0.9996 |
| cagr | -0.9550 |
| net_avg_win | 8.0959 |
| net_avg_loss | -16.9451 |
| avg_hold_time_bars | 2.8893 |
| exposure | 0.1936 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
