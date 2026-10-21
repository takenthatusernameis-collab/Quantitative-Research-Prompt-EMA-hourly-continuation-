# EMA Hourly Continuation — XTZ/USDT P100_200

**Symbol:** XTZ/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.6787 |
| net_win_rate | 0.4833 |
| gross_profit_factor | 0.9088 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -1.8378 |
| sortino_ratio | -0.4309 |
| max_drawdown | 0.3993 |
| cagr | -0.1795 |
| net_avg_win | 63.6353 |
| net_avg_loss | -87.6876 |
| avg_hold_time_bars | 12.3792 |
| exposure | 0.1514 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
