# EMA Hourly Continuation — FIDA/USDT P89_200

**Symbol:** FIDA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.6872 |
| net_win_rate | 0.4673 |
| gross_profit_factor | 0.8790 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -2.1272 |
| sortino_ratio | -0.5413 |
| max_drawdown | 0.4819 |
| cagr | -0.2211 |
| net_avg_win | 68.5055 |
| net_avg_loss | -87.4393 |
| avg_hold_time_bars | 14.0810 |
| exposure | 0.2045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
