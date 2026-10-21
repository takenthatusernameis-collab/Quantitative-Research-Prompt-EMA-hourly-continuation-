# EMA Hourly Continuation — CRV/USDT P12_144

**Symbol:** CRV/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.8388 |
| net_win_rate | 0.4945 |
| gross_profit_factor | 0.9869 |
| gross_win_rate | 0.4945 |
| sharpe_ratio | -0.9770 |
| sortino_ratio | -0.2315 |
| max_drawdown | 0.3219 |
| cagr | -0.1027 |
| net_avg_win | 91.1054 |
| net_avg_loss | -106.2743 |
| avg_hold_time_bars | 59.8073 |
| exposure | 0.7476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
