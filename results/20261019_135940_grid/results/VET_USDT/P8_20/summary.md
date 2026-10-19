# EMA Hourly Continuation — VET/USDT P8_20

**Symbol:** VET/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1699 |
| net_profit_factor | 0.3027 |
| net_win_rate | 0.4173 |
| gross_profit_factor | 0.7636 |
| gross_win_rate | 0.4479 |
| sharpe_ratio | -13.1456 |
| sortino_ratio | -7.6491 |
| max_drawdown | 0.9999 |
| cagr | -0.9803 |
| net_avg_win | 6.1236 |
| net_avg_loss | -14.4860 |
| avg_hold_time_bars | 2.7128 |
| exposure | 0.2095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
