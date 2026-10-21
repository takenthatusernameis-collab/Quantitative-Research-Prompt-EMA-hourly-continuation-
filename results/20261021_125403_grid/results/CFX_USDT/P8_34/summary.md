# EMA Hourly Continuation — CFX/USDT P8_34

**Symbol:** CFX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.7785 |
| net_win_rate | 0.5044 |
| gross_profit_factor | 1.0157 |
| gross_win_rate | 0.5044 |
| sharpe_ratio | -2.1345 |
| sortino_ratio | -0.8039 |
| max_drawdown | 0.6195 |
| cagr | -0.3083 |
| net_avg_win | 61.1600 |
| net_avg_loss | -79.9390 |
| avg_hold_time_bars | 9.7195 |
| exposure | 0.3040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
