# EMA Hourly Continuation — XNO/USDT P8_144

**Symbol:** XNO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.5223 |
| net_win_rate | 0.4136 |
| gross_profit_factor | 0.7540 |
| gross_win_rate | 0.4164 |
| sharpe_ratio | -6.0316 |
| sortino_ratio | -2.2370 |
| max_drawdown | 0.9354 |
| cagr | -0.6641 |
| net_avg_win | 35.0277 |
| net_avg_loss | -47.3002 |
| avg_hold_time_bars | 21.5028 |
| exposure | 0.6900 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
