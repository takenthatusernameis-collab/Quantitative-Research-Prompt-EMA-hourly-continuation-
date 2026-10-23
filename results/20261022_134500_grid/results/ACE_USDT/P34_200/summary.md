# EMA Hourly Continuation — ACE/USDT P34_200

**Symbol:** ACE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.8189 |
| net_win_rate | 0.5086 |
| gross_profit_factor | 1.0534 |
| gross_win_rate | 0.5143 |
| sharpe_ratio | -1.1042 |
| sortino_ratio | -0.2928 |
| max_drawdown | 0.3267 |
| cagr | -0.1294 |
| net_avg_win | 74.9332 |
| net_avg_loss | -94.6979 |
| avg_hold_time_bars | 32.9171 |
| exposure | 0.5214 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
