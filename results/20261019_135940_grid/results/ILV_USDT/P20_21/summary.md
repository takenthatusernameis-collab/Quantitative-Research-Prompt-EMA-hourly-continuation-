# EMA Hourly Continuation — ILV/USDT P20_21

**Symbol:** ILV/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1185 |
| net_profit_factor | 0.1219 |
| net_win_rate | 0.3046 |
| gross_profit_factor | 0.5233 |
| gross_win_rate | 0.3865 |
| sharpe_ratio | -17.2169 |
| sortino_ratio | -8.9907 |
| max_drawdown | 1.0000 |
| cagr | -0.9931 |
| net_avg_win | 3.8440 |
| net_avg_loss | -13.8200 |
| avg_hold_time_bars | 1.8852 |
| exposure | 0.1015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
