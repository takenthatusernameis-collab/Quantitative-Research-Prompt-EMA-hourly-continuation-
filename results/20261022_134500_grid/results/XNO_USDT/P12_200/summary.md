# EMA Hourly Continuation — XNO/USDT P12_200

**Symbol:** XNO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 577 |
| net_profit_factor | 0.5774 |
| net_win_rate | 0.4333 |
| gross_profit_factor | 0.8246 |
| gross_win_rate | 0.4350 |
| sharpe_ratio | -4.6469 |
| sortino_ratio | -1.5703 |
| max_drawdown | 0.8506 |
| cagr | -0.5283 |
| net_avg_win | 46.3770 |
| net_avg_loss | -61.4037 |
| avg_hold_time_bars | 25.5979 |
| exposure | 0.6714 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
