# EMA Hourly Continuation — CRV/USDT P20_144

**Symbol:** CRV/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.6673 |
| net_win_rate | 0.4709 |
| gross_profit_factor | 0.9814 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -3.6413 |
| sortino_ratio | -1.2143 |
| max_drawdown | 0.7837 |
| cagr | -0.4442 |
| net_avg_win | 57.9364 |
| net_avg_loss | -77.2704 |
| avg_hold_time_bars | 18.8536 |
| exposure | 0.4859 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
