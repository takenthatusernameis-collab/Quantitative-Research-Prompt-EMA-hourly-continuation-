# EMA Hourly Continuation — ONE/USDT P12_144

**Symbol:** ONE/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.7315 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 0.9804 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -2.4355 |
| sortino_ratio | -0.7180 |
| max_drawdown | 0.6205 |
| cagr | -0.2874 |
| net_avg_win | 74.6694 |
| net_avg_loss | -93.9871 |
| avg_hold_time_bars | 35.4083 |
| exposure | 0.7017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
