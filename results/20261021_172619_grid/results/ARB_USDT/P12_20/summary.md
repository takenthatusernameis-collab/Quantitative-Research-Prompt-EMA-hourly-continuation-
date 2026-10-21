# EMA Hourly Continuation — ARB/USDT P12_20

**Symbol:** ARB/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 249 |
| net_profit_factor | 0.6493 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 0.8830 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -2.1034 |
| sortino_ratio | -0.4745 |
| max_drawdown | 0.4340 |
| cagr | -0.1955 |
| net_avg_win | 66.6120 |
| net_avg_loss | -90.9263 |
| avg_hold_time_bars | 4.4739 |
| exposure | 0.0506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
