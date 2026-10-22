# EMA Hourly Continuation — TRX/USDT P8_55

**Symbol:** TRX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 932 |
| net_profit_factor | 0.3992 |
| net_win_rate | 0.4152 |
| gross_profit_factor | 1.0607 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -10.7761 |
| sortino_ratio | -4.6795 |
| max_drawdown | 0.9982 |
| cagr | -0.9186 |
| net_avg_win | 17.1361 |
| net_avg_loss | -30.4831 |
| avg_hold_time_bars | 11.0880 |
| exposure | 0.4697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
