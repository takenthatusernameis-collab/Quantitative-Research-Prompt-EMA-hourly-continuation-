# EMA Hourly Continuation — RLC/USDT P12_34

**Symbol:** RLC/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.7626 |
| net_win_rate | 0.5037 |
| gross_profit_factor | 1.0390 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -2.5257 |
| sortino_ratio | -0.9370 |
| max_drawdown | 0.7038 |
| cagr | -0.3492 |
| net_avg_win | 62.9168 |
| net_avg_loss | -83.7448 |
| avg_hold_time_bars | 7.4888 |
| exposure | 0.2277 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
