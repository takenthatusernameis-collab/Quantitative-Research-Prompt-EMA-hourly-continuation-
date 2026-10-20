# EMA Hourly Continuation — IOST/USDT P21_26

**Symbol:** IOST/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1154 |
| net_profit_factor | 0.1773 |
| net_win_rate | 0.3588 |
| gross_profit_factor | 0.7402 |
| gross_win_rate | 0.4263 |
| sharpe_ratio | -14.8095 |
| sortino_ratio | -7.3898 |
| max_drawdown | 1.0000 |
| cagr | -0.9816 |
| net_avg_win | 5.2038 |
| net_avg_loss | -16.4242 |
| avg_hold_time_bars | 2.3899 |
| exposure | 0.1254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
