# EMA Hourly Continuation — ZKJ/USDT P8_26

**Symbol:** ZKJ/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1706 |
| net_profit_factor | 0.2158 |
| net_win_rate | 0.2855 |
| gross_profit_factor | 0.5618 |
| gross_win_rate | 0.3570 |
| sharpe_ratio | -19.9289 |
| sortino_ratio | -11.9978 |
| max_drawdown | 1.0000 |
| cagr | -0.9987 |
| net_avg_win | 5.6500 |
| net_avg_loss | -10.4607 |
| avg_hold_time_bars | 4.0768 |
| exposure | 0.3161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
