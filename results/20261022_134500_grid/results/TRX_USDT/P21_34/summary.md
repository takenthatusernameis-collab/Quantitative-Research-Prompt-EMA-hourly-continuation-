# EMA Hourly Continuation — TRX/USDT P21_34

**Symbol:** TRX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 981 |
| net_profit_factor | 0.0953 |
| net_win_rate | 0.2487 |
| gross_profit_factor | 0.8095 |
| gross_win_rate | 0.4434 |
| sharpe_ratio | -17.7481 |
| sortino_ratio | -9.0203 |
| max_drawdown | 1.0000 |
| cagr | -0.9933 |
| net_avg_win | 4.3177 |
| net_avg_loss | -14.9979 |
| avg_hold_time_bars | 2.6045 |
| exposure | 0.1161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
