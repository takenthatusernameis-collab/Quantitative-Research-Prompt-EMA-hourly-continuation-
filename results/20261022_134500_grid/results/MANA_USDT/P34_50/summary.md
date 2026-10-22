# EMA Hourly Continuation — MANA/USDT P34_50

**Symbol:** MANA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 939 |
| net_profit_factor | 0.4066 |
| net_win_rate | 0.4175 |
| gross_profit_factor | 0.9421 |
| gross_win_rate | 0.4515 |
| sharpe_ratio | -9.8536 |
| sortino_ratio | -4.2896 |
| max_drawdown | 0.9961 |
| cagr | -0.8902 |
| net_avg_win | 17.4135 |
| net_avg_loss | -30.6894 |
| avg_hold_time_bars | 2.7796 |
| exposure | 0.1186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
