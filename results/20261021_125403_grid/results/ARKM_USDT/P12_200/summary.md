# EMA Hourly Continuation — ARKM/USDT P12_200

**Symbol:** ARKM/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.7775 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.8900 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -1.3714 |
| sortino_ratio | -0.3450 |
| max_drawdown | 0.3591 |
| cagr | -0.1478 |
| net_avg_win | 77.5758 |
| net_avg_loss | -90.0978 |
| avg_hold_time_bars | 51.3631 |
| exposure | 0.7331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
