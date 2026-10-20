# EMA Hourly Continuation — AMP/USDT P20_200

**Symbol:** AMP/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.4362 |
| net_win_rate | 0.4182 |
| gross_profit_factor | 0.6799 |
| gross_win_rate | 0.4259 |
| sharpe_ratio | -5.7767 |
| sortino_ratio | -2.0619 |
| max_drawdown | 0.9219 |
| cagr | -0.6316 |
| net_avg_win | 26.2216 |
| net_avg_loss | -43.2136 |
| avg_hold_time_bars | 20.6574 |
| exposure | 0.6085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
