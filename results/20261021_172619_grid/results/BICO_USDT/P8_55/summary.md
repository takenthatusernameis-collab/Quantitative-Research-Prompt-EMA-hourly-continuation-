# EMA Hourly Continuation — BICO/USDT P8_55

**Symbol:** BICO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 742 |
| net_profit_factor | 0.7229 |
| net_win_rate | 0.4852 |
| gross_profit_factor | 0.9113 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -2.5221 |
| sortino_ratio | -0.9801 |
| max_drawdown | 0.7097 |
| cagr | -0.3639 |
| net_avg_win | 49.1932 |
| net_avg_loss | -64.1343 |
| avg_hold_time_bars | 14.0836 |
| exposure | 0.4750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
