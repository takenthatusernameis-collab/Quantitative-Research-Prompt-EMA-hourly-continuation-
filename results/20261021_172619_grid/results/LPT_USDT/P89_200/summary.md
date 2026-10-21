# EMA Hourly Continuation — LPT/USDT P89_200

**Symbol:** LPT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.8047 |
| net_win_rate | 0.5055 |
| gross_profit_factor | 1.0172 |
| gross_win_rate | 0.5055 |
| sharpe_ratio | -1.1182 |
| sortino_ratio | -0.2659 |
| max_drawdown | 0.2944 |
| cagr | -0.1157 |
| net_avg_win | 78.7332 |
| net_avg_loss | -100.0027 |
| avg_hold_time_bars | 15.0945 |
| exposure | 0.1887 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
