# EMA Hourly Continuation — ONT/USDT P12_200

**Symbol:** ONT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.6790 |
| net_win_rate | 0.4460 |
| gross_profit_factor | 0.8052 |
| gross_win_rate | 0.4460 |
| sharpe_ratio | -2.2618 |
| sortino_ratio | -0.5986 |
| max_drawdown | 0.5220 |
| cagr | -0.2416 |
| net_avg_win | 67.6858 |
| net_avg_loss | -80.2552 |
| avg_hold_time_bars | 42.3665 |
| exposure | 0.6748 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
