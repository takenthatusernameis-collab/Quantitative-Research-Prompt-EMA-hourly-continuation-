# EMA Hourly Continuation — SKL/USDT P12_20

**Symbol:** SKL/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1603 |
| net_profit_factor | 0.3180 |
| net_win_rate | 0.4198 |
| gross_profit_factor | 0.8282 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -13.0880 |
| sortino_ratio | -7.4392 |
| max_drawdown | 0.9999 |
| cagr | -0.9778 |
| net_avg_win | 6.9274 |
| net_avg_loss | -15.7650 |
| avg_hold_time_bars | 2.1566 |
| exposure | 0.1571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
