# EMA Hourly Continuation — DUSK/USDT P12_144

**Symbol:** DUSK/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.7003 |
| net_win_rate | 0.4802 |
| gross_profit_factor | 0.9424 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -2.2551 |
| sortino_ratio | -0.6793 |
| max_drawdown | 0.5679 |
| cagr | -0.2730 |
| net_avg_win | 59.0640 |
| net_avg_loss | -77.9060 |
| avg_hold_time_bars | 33.9736 |
| exposure | 0.7011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
