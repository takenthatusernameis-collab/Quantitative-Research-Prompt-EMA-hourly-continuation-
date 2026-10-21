# EMA Hourly Continuation — XEC/USDT P26_144

**Symbol:** XEC/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.8256 |
| net_win_rate | 0.5158 |
| gross_profit_factor | 1.0700 |
| gross_win_rate | 0.5158 |
| sharpe_ratio | -1.3143 |
| sortino_ratio | -0.3971 |
| max_drawdown | 0.4627 |
| cagr | -0.1684 |
| net_avg_win | 76.8757 |
| net_avg_loss | -99.1806 |
| avg_hold_time_bars | 23.8514 |
| exposure | 0.4792 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
