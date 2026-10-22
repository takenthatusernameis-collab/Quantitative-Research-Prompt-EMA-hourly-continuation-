# EMA Hourly Continuation — TAO/USDT P21_34

**Symbol:** TAO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1149 |
| net_profit_factor | 0.4860 |
| net_win_rate | 0.4143 |
| gross_profit_factor | 0.9074 |
| gross_win_rate | 0.4404 |
| sharpe_ratio | -10.1721 |
| sortino_ratio | -4.8692 |
| max_drawdown | 0.9981 |
| cagr | -0.9158 |
| net_avg_win | 19.8256 |
| net_avg_loss | -28.8514 |
| avg_hold_time_bars | 2.3734 |
| exposure | 0.1240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
