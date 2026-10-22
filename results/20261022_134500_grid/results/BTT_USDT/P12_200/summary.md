# EMA Hourly Continuation — BTT/USDT P12_200

**Symbol:** BTT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.5164 |
| net_win_rate | 0.4578 |
| gross_profit_factor | 0.8740 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -3.5245 |
| sortino_ratio | -0.8665 |
| max_drawdown | 0.6819 |
| cagr | -0.3470 |
| net_avg_win | 49.7603 |
| net_avg_loss | -81.3628 |
| avg_hold_time_bars | 55.5682 |
| exposure | 0.7780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
